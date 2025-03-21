# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FlowMap
                                 A QGIS plugin
 flow map
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-12-25
        copyright            : (C) 2021 by Caner Güzeler
        email                : canerguzeler@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FlowMap class from file FlowMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .flow_map import FlowMap
    return FlowMap(iface)
