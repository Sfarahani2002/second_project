import simpy

env = simpy.Environment()

def Customer(env):
    yield env.timeout(30)
    print(f"Details entered bat time:{env.now}")
    yield env.timeout(60)
    print(f"Cash retrieved at time:{env.now}")

env.process(Customer(env=env))
env.run()
        