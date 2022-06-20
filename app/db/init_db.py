import logging
from sqalchemy.orm import Session

from app import crud, schemas
from app.db import base
from app.data.mock_data import TEST_DATA

logger = logging.getLogger(__name__)

FIRST_SUPER_USER = "admin@api.com"

def init_db(db: Session) -> None:
    """Инициализаия баз данных. в реальности данные буду подбираться из хранилища"""

    if FIRST_SUPER_USER:
        user = crud.user.get_by_email(db, email = FIRST_SUPER_USER)
        if not user:
            user_in = schemas.UserCreate(
                full_name = "Initial Super User",
                email = FIRST_SUPER_USER,
                is_superuser = True
            )
            user = crud.user.create(db, obj_in = user_in)
        else:
            logger.warning(f"skip creating superuser. {FIRST_SUPER_USER} exits")
        
        if not user.records:
            for record in TEST_DATA:
                recipe_in = schemas.RecordCreate(
                    label = record["label"],
                    source = record["source"],
                    url = record["url"],
                    submitter_id = user.id,

                )
                crud.record.create(db, obj_in = record_id)
    else:
        logger.warning("Skipping creating users, no FIRST_SUPERUSER provided")