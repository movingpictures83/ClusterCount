import PyPluMA

class ClusterCountPlugin:
   def input(self, filename):
      parameterfile = open(filename, 'r')
      self.parameters = dict()
      for line in parameterfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if (len(PyPluMA.prefix()) != 0):
         self.parameters['inputfile'] = PyPluMA.prefix() + "/" + self.parameters['inputfile'] # Possibly append prefix

   def run(self):
      clusterfile = open(self.parameters['inputfile'], 'r')
      self.threshold = int(self.parameters['threshold'])
      self.count = 0
      members = 0
      for line in clusterfile:
         if (line.strip() == '\"\",\"x\"'):
            if (members >= self.threshold):
               self.count += 1
               members = 0
         else:
            members += 1
      if (members >= self.threshold):  # Last one
         self.count += 1

   def output(self, filename):
      print("NUMBER OF CLUSTERS ("+self.parameters['inputfile']+", THRESHOLD="+str(self.threshold)+"): "+str(self.count))
