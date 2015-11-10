###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from .RabbitMQComponent import RabbitMQComponent


class RabbitMQVHostAPI(RabbitMQComponent):
    meta_type = "RabbitMQVHostAPI"
    portal_type = "RabbitMQVHost"

    _relations = RabbitMQComponent._relations + (
        ('rabbitmq_apinode', ToOne(ToManyCont,
            'ZenPacks.zenoss.RabbitMQ.RabbitMQNodeAPI.RabbitMQNodeAPI',
            'rabbitmq_apivhosts',
            ),),
        ('rabbitmq_apiexchanges', ToManyCont(ToOne,
            'ZenPacks.zenoss.RabbitMQ.RabbitMQExchangeAPI.RabbitMQExchangeAPI',
            'rabbitmq_apivhost',
            ),),
        ('rabbitmq_apiqueues',ToManyCont(ToOne,
            'ZenPacks.zenoss.RabbitMQ.RabbitMQQueueAPI.RabbitMQQueueAPI',
            'rabbitmq_apivhost',
	    ),),
        )

    def device(self):
        return self.rabbitmq_apinode().device()
