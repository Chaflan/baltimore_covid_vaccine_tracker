from baltimore_covid_vaccine_tracker import scraper
from baltimore_covid_vaccine_tracker import particle_simulator


if __name__ == '__main__':
	num_particles = 60
	radii = 0.008

	percent_first_shot, percent_second_shot = scraper.scrape()
	print("Percent Vaccinations: {0:.1f}% first shot, {1:.1f}% second shot".format(
		percent_first_shot, percent_second_shot))

	percent_green = percent_second_shot
	percent_yellow = percent_first_shot - percent_second_shot
	percent_red = 100 - percent_yellow - percent_green
	print("Percent Particles: {0:.1f}% red, {1:.1f}% yellow, {2:.1f}% green".format(
		percent_red, percent_yellow, percent_green))

	num_red = round(num_particles * percent_red / 100)
	num_yellow = round(num_particles * percent_yellow / 100)
	num_green = round(num_particles * percent_green / 100)
	print("Num Particles: {0} red + {1} yellow + {2} green = {3} total".format(
		num_red, num_yellow, num_green, num_particles))

	styles = {'color': 'tab:red'}
	sim = particle_simulator.Simulation()
	sim.add_particles(num_red, radii, {'color': 'tab:red'})
	sim.add_particles(num_yellow, radii, {'color': '#FFEF00'})
	sim.add_particles(num_green, radii, {'color': 'tab:green'})
	sim.do_animation(save=False)
