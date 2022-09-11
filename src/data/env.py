import gym
import numpy as np
# Modifying wrapper around the LTS (Long Term Satisfaction) env:
# - allows us to tweak the user model (and thus: reward behavior)
# - adds user's current satisfaction value to observation

"""
Wrapper del entorno del LTS (Long Term Satisfaction) que nos permite extraer la información
de la satisfacción del usuario y modificar la recompensa para nuestro análisis.
"""
class LTSWrapperEnvDefault(gym.ObservationWrapper):

    def __init__(self, env,env_update_config=None):
        # Tweak incoming environment.
        if env_update_config is not None:
            env.environment._user_model._user_sampler._state_parameters.update(
            env_update_config
            )

        super().__init__(env)

        # Adjust observation space.
        if "response" in self.observation_space.spaces:
            self.observation_space.spaces["user"] = gym.spaces.Box(0.0, 1.0, (1, ), dtype=np.float32)
            for r in self.observation_space["response"]:
                if "engagement" in r.spaces:
                    r.spaces["watch_time"] = r.spaces["engagement"]
                    del r.spaces["engagement"]
                    break

    def observation(self, observation):
        if "response" in self.observation_space.spaces:
            observation["user"] = np.array([self.env.environment._user_model._user_state.satisfaction])
            for r in observation["response"]:
                if "engagement" in r:
                    r["watch_time"] = r["engagement"]
                    del r["engagement"]
        return observation


               
               
               
               
               
               
                   

class LTSWithStrongerDissatisfactionEffect(LTSWrapperEnvDefault):
    def __init__(self, env):
        env_update_config = {
            "sensitivity": 0.058, # default sensitivity=0.01, dependencia del estado latente con la magnitud del engagement
            "time_budget": 120, # default time_budget=60, tamaño de la sesión del usuario
            "choc_stddev": 0.1, # choc_stddev=1.0, std del engagement con contenido no click-bait
            "kale_stddev": 0.1, # default kale_stddev=1.0, std del engagement con contenido click-bait
            #"innovation_stddev": 0.01, # default innovation_stddev=0.05
            #"choc_mean": 1.25, # default choc_mean=5.0, engagement medio con contenido no click-bait.
            #"kale_mean": 1.0, # default kale_mean=4.0, engagement medio con el contenido de clickbait.
            #"memory_discount": 0.9, # default memory_discount=0.7

        }
        super().__init__(env,env_update_config = env_update_config)


 