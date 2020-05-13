
class ClusterCountPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      clusterfile = open(self.myfile, 'r')
      self.count = 0
      for line in clusterfile:
         if (line.strip() == '\"\",\"x\"'):
            self.count += 1

   def output(self, filename):
      print("NUMBER OF CLUSTERS ("+self.myfile+"): "+str(self.count))
