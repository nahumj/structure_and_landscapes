from unittest import TestCase as TC
import tempfile
import os
import shutil

from integer.integer_organism import Organism as int_organism
from population.population import Population

import run
import persistence


class TestRun(TC):
    def setUp(self):
        """
        Generates a temp file path.
        """
        temp_dir = tempfile.mkdtemp()
        filename = "test.shelf"
        filepath = os.path.join(temp_dir, filename)
        self.temp_file = filepath

    def tearDown(self):
        """
        Closes temp file.
        """
        temp_dir = os.path.dirname(self.temp_file)
        shutil.rmtree(temp_dir)

    def test_run_simple(self):
        org_list = [int_organism(i) for i in range(1, 11)]
        init_pop = Population(org_list)
        parameters = {"generations" : 5}
        r = run.Run(init_pop, parameters, self.temp_file)
        r.run()
        with persistence.get_shelf(self.temp_file) as shelf:
            r_saved = shelf.values()[0]
            self.assertEquals(r_saved.parameters["generations"], 5)
            self.assertNotEquals(r_saved.final_population, None)