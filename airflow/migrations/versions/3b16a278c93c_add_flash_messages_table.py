#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add flash messages table

Revision ID: 3b16a278c93c
Revises: e1a11ece99cc
Create Date: 2020-09-28 11:50:11.350033

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3b16a278c93c'
down_revision = 'e1a11ece99cc'
branch_labels = None
depends_on = None


def upgrade():
    """Apply add flash messages table"""
    op.create_table('flash_messages',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.String(length=1024), nullable=False),
                    sa.Column('category', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id'))


def downgrade():
    """Unapply add flash messages table"""
    op.drop_table('flash_messages')
