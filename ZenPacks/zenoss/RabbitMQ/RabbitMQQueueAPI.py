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

class RabbitMQQueueAPI(RabbitMQComponent):
    meta_type =  "RabbitMQQueueAPI"
    portal_type = "RabbitMQAPIQueue"

    # Modeled attributes.
    durable = None
    auto_delete = None
    arguments = None
    api = False
    state = 'running'
    # Managed attributes.
    threshold_messages_max = None

    _properties = RabbitMQComponent._properties + (
        {'id': 'durable', 'type': 'boolean', 'mode': 'w'},
        {'id': 'auto_delete', 'type': 'boolean', 'mode': 'w'},
        {'id': 'arguments', 'type': 'string', 'mode': 'w'},
        {'id': 'threshold_messages_max', 'type': 'int', 'mode': 'w'},
        {'id': 'state', 'type': 'string', 'mode': 'w'},
        {'id': 'api', 'type': 'boolean', 'mode': 'w'},
        )

    _relations = RabbitMQComponent._relations + (
        ('rabbitmq_apivhost', ToOne(ToManyCont,
            'ZenPacks.zenoss.RabbitMQ.RabbitMQVHostAPI.RabbitMQVHostAPI',
            'rabbitmq_apiqueues',
            ),),
        )

    def device(self):
        return self.rabbitmq_apivhost().device()

    @property
    def rabbitmq_node_name(self):
        return self.rabbitmq_apivhost().rabbitmq_apinode().title

    @property
    def rabbitmq_vhost_name(self):
        return self.rabbitmq_apivhost().title

