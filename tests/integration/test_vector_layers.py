from mock import MagicMock, patch
import os
import unittest

from qgis.core import QgsProject, QgsVectorLayer
from tests.integration.roadnet_test_cases import QgisTestCase
import vector_layers
import roadnet_exceptions as rn_except


class TestVectorLayers(QgisTestCase):
    def tearDown(self):
        """
        Remove vector layers that have been added by tests.
        """
        registry = QgsProject.instance()
        registry.removeAllMapLayers()

    def test_add_styled_spatialite_layer(self):
        display_name = 'esu'
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')

        vector_layers.add_styled_spatialite_layer(
            vlayer_name='esu',
            display_name=display_name,
            db_path=db_path,
            iface=self.iface)

        registry = QgsProject.instance()
        layers = registry.mapLayersByName(display_name)
        layer_count = len(layers)
        layer_name = layers[0].name()
        self.assertEqual(layer_count, 1,
                         "One layer was not loaded ({})".format(len(layers)))
        self.assertEqual(layer_name, display_name,
                         "Loaded name was not {} ({})".format(display_name,
                                                              layer_name))

    @patch.object(rn_except.QMessageBoxWarningError, 'show_message_box')
    def test_add_styled_spatialite_layer_invalid_style(self, mock_error):
        display_name = 'esu'
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')

        vector_layers.add_styled_spatialite_layer(
            vlayer_name='esu',
            display_name=display_name,
            db_path=db_path,
            iface=self.iface,
            style='This does not exist')

        registry = QgsProject.instance()
        layers = registry.mapLayersByName(display_name)
        self.assertEqual(len(layers), 1,
                         "Failed to load layer with invalid style")

    @patch.object(rn_except.QMessageBoxWarningError, 'show_message_box')
    def test_add_styled_spatialite_layer_invalid_layer_error(self, mock_error):
        # Arrange
        display_name = 'test_esu'
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')

        # Act
        with self.assertRaises(rn_except.InvalidLayerPopupError):
            vector_layers.add_styled_spatialite_layer(
                vlayer_name='this does not exist',
                display_name=display_name,
                db_path=db_path,
                iface=self.iface)

    @patch.object(rn_except.QMessageBoxWarningError, 'show_message_box')
    def test_apply_layer_style_invalid(self, mock_error):
        # Arrange
        vlayer = MagicMock(spec=QgsVectorLayer)
        style = 'this style does not exist'
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')

        # Act
        with self.assertRaises(rn_except.InvalidStylePopupError):
            vector_layers.apply_layer_style(vlayer, style, db_path)

    def test_remove_spatialite_layer(self):
        # Add a new layer to remove
        display_name = 'esu'
        registry = QgsProject.instance()
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')
        vl = vector_layers.add_styled_spatialite_layer(
            vlayer_name='esu',
            display_name=display_name,
            db_path=db_path,
            iface=self.iface)

        # Act
        vector_layers.remove_spatialite_layer(vl, self.iface)

        # Assert
        layers = registry.mapLayersByName(display_name)
        layer_count = len(layers)
        self.assertEqual(layer_count, 0,
                         "Layer was not removed ({} layers found)".format(len(layers)))

    @patch.object(rn_except.QMessageBoxWarningError, 'show_message_box')
    def test_remove_spatialite_layer_non_existent(self, mock_error):
        # Add a new layer to remove
        display_name = 'esu'
        registry = QgsProject.instance()
        roadnet_dir = os.path.dirname(os.path.abspath(vector_layers.__file__))
        db_path = os.path.join(roadnet_dir, 'database_files', 'roadnet_demo.sqlite')
        vl = vector_layers.add_styled_spatialite_layer(
            vlayer_name='esu',
            display_name=display_name,
            db_path=db_path,
            iface=self.iface)
        registry.removeMapLayer(vl.id())  # Removes layer

        # Act and Assert
        with self.assertRaises(rn_except.QMessageBoxWarningError):
            vector_layers.remove_spatialite_layer(vl, self.iface)


if __name__ == '__main__':
    unittest.main()
