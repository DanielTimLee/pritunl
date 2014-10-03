from pritunl.setup.local import setup_local
from pritunl.setup.app import setup_app
from pritunl.setup.mongo import setup_mongo
from pritunl.setup.temp_path import setup_temp_path
from pritunl.setup.logger import setup_logger
from pritunl.setup.public_ip import setup_public_ip
from pritunl.setup.handlers import setup_handlers
from pritunl.setup.poolers import setup_poolers
from pritunl.setup.host import setup_host
from pritunl.setup.runners import setup_runners
from pritunl.setup.server_cert import setup_server_cert
from pritunl.settings import settings

def setup_all():
    setup_local()
    setup_app()
    setup_mongo()
    setup_temp_path()
    setup_logger()
    setup_public_ip()
    setup_handlers()
    setup_poolers()
    setup_host()
    setup_runners()

    if settings.conf.ssl:
        setup_server_cert()
