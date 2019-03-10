import random
from multiprocessing import Process
from MAMEToolkit.sf_environment import Environment

roms_path = "roms/sfa3.zip"
workers= 1

def run_env(worker_id, roms_path):
	env = Environment(f"env{worker_id}", roms_path)
	env.start()
	while True:
		move_action = random.randint(0,8)
		attack_action = random.randint(0,9)
		frames, reward, round_done, stage_done, game_done = env.step(move_action, attack_action)
		if game_done:
			env.new_game()
		elif stage_done:
			env.next_stage()
		elif round_done:
			env.next_round()


if __name__ == '__main__':
	# Environments must be created outside of the threads
	#threads = [Process(target=run_env, args=(i, roms_path)) for i in range(workers)]
	#[thread.start() for thread in threads]

	env = Environment("env1", roms_path)
	env.start()
	while True:
		move_action = random.randint(0,8)
		attack_action = random.randint(0,9)
		frames, reward, round_done, stage_done, game_done = env.step(move_action, attack_action)
		if game_done:
			env.new_game()
		elif stage_done:
			env.next_stage()
		elif round_done:
			env.next_round()
