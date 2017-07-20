from particleSwarmOptimization.particle import Particle
from particleSwarmOptimization.chaoticParticle import ChaoticParticle


class PSO(object):

    def __init__(self,costFunc,num_dimensions,bounds,num_particles,maxiter,weight,cognativeConstant,socialConstant):
        self.__num_dimensions = num_dimensions
        self.__err_best_g = -1                   # best error for group
        self.__pos_best_g = []                   # best position for group
        self.__maxiter = maxiter
        self.__num_particles = num_particles
        self.__bounds = bounds
        self.__costFunc = costFunc
        self.__weight = weight
        self.__cognitiveConstant = cognativeConstant
        self.__socialConstant = socialConstant

    def establishSwarm(self):
        self.__swarm = []
        for i in range(0, self.__num_particles):
            self.__swarm.append(ChaoticParticle(self.__bounds, self.__num_dimensions, self.__costFunc, self.__weight, self.__cognitiveConstant, self.__socialConstant))


    def setGlobalBest(self):
        # print i,err_best_g
        # cycle through particles in __swarm and evaluate fitness
        print('[')
        for j in range(0, self.__num_particles):
            self.__swarm[j].evaluate()
            print(self.__swarm[j].toString())

            # determine if current particle is the best (globally)
            if self.__swarm[j].err_i < self.__err_best_g or self.__err_best_g == -1:
                self.__pos_best_g = list(self.__swarm[j].position_i)
                self.__err_best_g = float(self.__swarm[j].err_i)
        print(']')

    def begin(self):
        # begin optimization loop
        i=0
        while i < self.__maxiter:
            self.setGlobalBest()

            # cycle through __swarm and update velocities and position
            for j in range(0,self.__num_particles):
                self.__swarm[j].update_velocity(self.__pos_best_g)
                self.__swarm[j].update_position()
            i+=1
            self.printGlobalBest()

        print('FINAL:')
        self.printGlobalBest()


    def printGlobalBest(self):
        print(self.__pos_best_g)
        print(self.__err_best_g)