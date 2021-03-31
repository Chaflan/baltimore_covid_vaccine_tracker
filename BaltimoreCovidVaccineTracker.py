from BaltimoreCovidVaccineTracker import Scraper
from BaltimoreCovidVaccineTracker import ParticleSimulator

if __name__ == '__main__':
	nparticles = 110
	radii = 0.008

	percentFirstShot, percentSecondShot = Scraper.scrape()

	percentGreen = percentSecondShot
	percentYellow = percentFirstShot - percentSecondShot
	percentRed = 100 - percentYellow - percentGreen
	print("Percents: ", percentRed, "% red ", percentYellow, "% yellow ", percentGreen, "% green", sep='')

	numRed = round(nparticles * percentRed / 100)
	numYellow = round(nparticles * percentYellow / 100)
	numGreen = round(nparticles * percentGreen / 100)
	print("Numbers: ", numRed, " red + ", numYellow, " yellow + ", numGreen, " green = ", nparticles, " total", sep='')

	styles = {'color': 'tab:red'}
	sim = ParticleSimulator.Simulation(nparticles, radii, styles)
	sim.add_particles(numRed, radii, {'color': 'tab:red'})
	sim.add_particles(numYellow, radii, {'color': '#FFEF00'})
	sim.add_particles(numGreen, radii, {'color': 'tab:green'})
	sim.do_animation(save=False)
