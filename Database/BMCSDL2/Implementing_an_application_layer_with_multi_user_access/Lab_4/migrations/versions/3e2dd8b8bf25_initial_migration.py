"""Initial migration

Revision ID: 3e2dd8b8bf25
Revises: 
Create Date: 2024-11-12 12:38:57.247010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e2dd8b8bf25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operation_type', sa.String(length=10), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('changed_data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.Date(), nullable=False),
    sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warehouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('warehouse_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['warehouse_id'], ['warehouse.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_product',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'product_id'),
    info={'bind_key': None}
    )
    op.create_table('supplier_product',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('supplier_id', 'product_id'),
    info={'bind_key': None}
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplier_product')
    op.drop_table('order_product')
    op.drop_table('product')
    op.drop_table('warehouse')
    op.drop_table('order')
    op.drop_table('supplier')
    op.drop_table('log')
    op.drop_table('employee')
    op.drop_table('customer')
    # ### end Alembic commands ###