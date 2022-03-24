import unittest
from motorcycle_klasy import Motorcycle, SportMotorcycle, Tyre, Suspension


class TestMoto(unittest.TestCase):

    def setUp(self):
        self.val = Motorcycle("Yamaha", "R6", 600, 120, 180, 260, 3.2, 22)
        self.mar = SportMotorcycle("Honda", "CBR", 100, 190)

    def test_show_brand(self):
        self.assertEqual(self.val.brand + self.val.model, "Yamaha" + "R6")

    def test_speck(self):
        self.assertEqual(self.val.speck(), ('Yamaha R6\n'
                                            'Weight : 180 kg\n'
                                            'Top speed : 260 kmh\n'
                                            'Acceleration 0-100 : 3.2 s\n'
                                            'HP: 120\n' 
                                            'Fitted with set of all weather tyre and suspension is on medium settings.'))

        self.assertEqual(self.mar.speck(), ('Honda CBR\n'
                                            'Weight : 180 kg\n'
                                            'Top speed : 260 kmh\n'
                                            'Acceleration 0-100 : 3.2 s\n'
                                            'HP: 190\n'
                                            'Fitted with set of all weather tyre and suspension is on medium settings.'))

    def test_exhaust(self):
        self.assertEqual(self.val.hp, 120)
        self.assertEqual(self.mar.hp, 190)

        self.val.sport_exhaust()
        self.mar.sport_exhaust()

        self.assertEqual(self.val.hp, 140)
        self.assertEqual(self.mar.hp, 210)

    def test_slick_tyre(self):

        self.assertTrue(self.val.slick_tyre(), "slick tyre fitted")

    def test_wet_tyre(self):

        self.assertFalse(self.val.wet_tyre(), "wet tyre fitted")

    def test_rain(self):

        with self.assertRaises(AssertionError, msg="motorcycle fitted with dry tyre"):
            self.assertFalse(self.val.wet_tyre())
            self.assertFalse(self.mar.slick_tyre())

    def test_off_road_settings(self):
        self.assertEqual(self.val.suspension, Suspension.road)
        self.assertEqual(self.val.tyre, Tyre.all)
        self.assertEqual(self.mar.suspension, Suspension.road)
        self.assertEqual(self.mar.tyre, Tyre.all)

        self.val.off_road_settings()
        self.mar.off_road_settings()

        self.assertEqual(self.val.suspension, Suspension.dirt)
        self.assertEqual(self.val.tyre, Tyre.off_road)
        self.assertEqual(self.mar.suspension, Suspension.dirt)
        self.assertEqual(self.val.tyre, Tyre.off_road)

    def test_track_settings(self):
        self.assertEqual(self.val.suspension, Suspension.road)
        self.assertEqual(self.val.tyre, Tyre.all)
        self.assertEqual(self.mar.suspension, Suspension.road)
        self.assertEqual(self.mar.tyre, Tyre.all)

        self.val.track_settings()
        self.mar.track_settings()

        self.assertEqual(self.val.suspension, Suspension.track)
        self.assertEqual(self.val.tyre, Tyre.slick)
        self.assertEqual(self.mar.suspension, Suspension.track)
        self.assertEqual(self.val.tyre, Tyre.slick)

    def test_lose_weight(self):
        self.assertEqual(self.val.weight, 180)
        self.assertEqual(self.val.acceleration, 3.2)
        self.assertEqual(self.mar.weight, 180)
        self.assertEqual(self.mar.acceleration, 3.2)

        self.val.lose_weight()
        self.mar.lose_weight()

        self.assertEqual(self.val.weight, 170)
        self.assertEqual(self.val.acceleration, 3)
        self.assertEqual(self.mar.weight, 170)
        self.assertEqual(self.mar.acceleration, 3)


if __name__ == '__main__':
    unittest.main()

