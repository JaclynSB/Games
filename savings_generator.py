import random
import numpy as np
import matplotlib.pyplot as plt

class Savings():
    def __init__(self, start, monthly, years, trials):
        self.start = start #how much money you start with
        self.monthly = monthly #how much you want to invest each month
        self.years = years #how many years out you want to look
        self.trials = trials #how many trials to complete
        self.yearly_sav = []
        self.end_sav = []
        self.yr_list = []
        self.avgs_list = []
    
    def trial_data(self):
        """
        Runs a trial self.trials number of times and returns
        yearly_sav which holds each year's results for every trial, and
        end_sav which holds the final end savings for every trial
        """
        for trial in range(self.trials):
            new_val = self.start
            sav = []
            for year in range(self.years):
                for month in range(12): #want to see yearly values based on monthly inputs and growth
                    interest = random.randint(-1,2)
                    new_val = new_val + self.monthly
                    new_val = new_val + (new_val * (0.01*interest))
                    end_val = new_val
                sav.append(round(end_val,2)) #appends each year's end value to sav list
            self.end_sav.append(round(end_val,2))
            self.yearly_sav.append(sav)
        # print(self.yearly_sav)
    
    def list_by_years(self):
        """
        Returns a list of lists
        Each inner list contains the savings for that given year
        Where list[i], [i] is the year and list[i][j], [j] is the savings
        """
        self.trial_data()
        for year in range(self.years):
            new_lst = []
            for item in self.yearly_sav:
                new_lst.append(int(item[year]))
            self.yr_list.append(new_lst)
            
    def yr_avgs(self):
        """
        Returns a single list where each value is the mean savings 
        of all the trials for that year
        """
        self.list_by_years()
        for item in self.yr_list:
            avg = np.mean(item)
            self.avgs_list.append(avg)
        # print(self.avgs_list)
        
    def graph_results(self):
        """
        Returns a histogram of all generated end savings 
        over the given number of years
        """
        self.trial_data()
        plt.hist(self.end_sav, bins = 20)   
        plt.xlabel('Starting with: $' + str(self.start) + '\nadding $' + str(self.monthly) + ' per month over ' + str(self.years) + ' years')
        plt.ylabel('Number of instances out of '+ str(self.trials))
        plt.show()
        
    def graph_avg_growth(self):
        self.yr_avgs()
        yr_lst = [i+1 for i in range(self.years)]
        plt.plot(yr_lst, self.avgs_list)
        plt.xlabel('Number of years')
        plt.ylabel('Savings')
        plt.show()

save = Savings(25000, 750, 35, 10000)
save.graph_results()
save.graph_avg_growth()