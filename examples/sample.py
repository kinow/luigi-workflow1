import luigi

class TaskA(luigi.Task):

	name = luigi.Parameter()

	def output(self):
		return luigi.LocalTarget('/home/kinow/Downloads/test_luigi.txt')

	def requires(self):
		return None

	def run(self):
		print("Hello world {}!".format(self.name))

if __name__ == "__main__":
    luigi.run()
