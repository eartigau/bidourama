    import numpy as np
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    from astropy.table import Table

    spx = Table.read('spx.csv', format='csv')

    age = 49
    retire = 60
    death = 90

    market_mean = 0.12
    inflation_mean = 0.02
    volatility = 0.19/2

    starting_pot = 200000

    nmc = 100

    year_saving = 6000
    width_draw_frac = 0.04


    samples = []
    for imc in tqdm(range(nmc)):
        sample = []
        pot = starting_pot
        for year in range(age, death):
            if year < retire:
                pot = pot * (1 + np.random.normal(market_mean-inflation_mean, volatility)) + year_saving
            else:
                pot = pot * (1 + np.random.normal(market_mean-inflation_mean, volatility))
                widthdraw = pot * width_draw_frac
                pot = pot - widthdraw
            #plt.plot(year, pot, 'x', color='blue')
            sample.append(pot)

        samples.append(sample)

    samples = np.array(samples)
    plt.plot( samples.T, color='blue', alpha=0.1)


    plt.xlabel('Age')
    plt.ylabel('Pension Pot')
    plt.title('Monte Carlo Simulation of Pension Pot at Death')
    plt.grid()
    plt.show()