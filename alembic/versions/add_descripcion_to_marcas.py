
from alembic import op
import sqlalchemy as sa


revision = '1234'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('marcas', sa.Column('descripcion', sa.Text(), nullable=True))

def downgrade():
    op.drop_column('marcas', 'descripcion')
