import abc
from sqlalchemy import text
from db_plugins.db.sql.models import AstroObject, Classification, Xmatch
from astropy import units

class ObjectQuery(abc.ABC):
    @abc.abstractmethod
    def query_objects(self):
        pass


class SQLObjectQuery(ObjectQuery):
    def __init__(self, db):
        self.db = db

    def query_objects(self, args):
        params = self.parse_parameters(args)
        conesearch_args = self._parse_conesearch_args(args)
        paginated = self._get_objects(params, conesearch_args).paginate(
            args["page"], args["page_size"], args["count"]
        )
        return paginated

    def _get_objects(self, params, conesearch_args):
        return (
            self.db.session.query(AstroObject, Classification)
            .outerjoin(AstroObject.classifications)
            .filter(*params)
            .params(**conesearch_args)
        )

    def parse_parameters(self, args):
        classifier, class_, ndet, firstmjd, lastmjd, probability, conesearch = (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
        for arg in args:
            if args[arg] is not None:
                if arg == "classifier":
                    classifier = Classification.classifier_name == args[arg]
                if arg == "class":
                    class_ = Classification.class_name == args[arg]
                if arg == "ndet":
                    ndet = AstroObject.nobs >= args[arg][0]
                    if len(args[arg]) > 1:
                        ndet = ndet & (AstroObject.nobs <= args[arg][1])
                if arg == "firstmjd":
                    firstmjd = AstroObject.firstmjd >= args[arg][0]
                    if len(args[arg]) > 1:
                        firstmjd = firstmjd & (AstroObject.firstmjd <= args[arg][1])
                if arg == "lastmjd":
                    lastmjd = AstroObject.lastmjd >= args[arg][0]
                    if len(args[arg]) > 1:
                        lastmjd = lastmjd & (AstroObject.lastmjd <= args[arg][1])
                if arg == "probability":
                    probability = Classification.probability >= args[arg]
        conesearch = self._create_conesearch_statement(args)
        return classifier, class_, ndet, firstmjd, lastmjd, probability, conesearch

    def _create_conesearch_statement(self, args):
        try:
            ra, dec, radius = args["ra"], args["dec"], args["radius"]
        except KeyError as e:
            ra, dec, radius = None, None, None

        if ra and dec and radius:
            return text("q3c_radial_query(meanra, meandec,:ra, :dec, :radius)")
        else:
            return True

    def _parse_conesearch_args(self, args):
        try:
            ra, dec, radius = args["ra"], args["dec"], args["radius"]
        except KeyError as e:
            ra, dec, radius = None, None, None

        if ra and dec and radius:
            radius = radius * units.arcsec
            radius = radius.to(units.deg)
            radius = radius.value
        return {"ra": ra, "dec": dec, "radius": radius}