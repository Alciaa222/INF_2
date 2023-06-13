# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NewPlugin
                                 A QGIS plugin
 Wtyczka oblicza różnicę wysokości oraz pole powierzchni między punktami
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-12
        copyright            : (C) 2023 by Nikola Bobik Alicja Dymowska Andżelika Bańkowska
        email                : nikola.bobik2@gmail.com
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
    """Load NewPlugin class from file NewPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .new_plugin import NewPlugin
    return NewPlugin(iface)
