# Librerías estandar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import time
from tqdm import tqdm



def run_random_walk_episode(env, agg_func = np.sum) -> float:
    """
    Función que ejecuta un episodio de un agente random walk
    @param env: entorno del agente
    @param agg_func: función de agregación de los rewards
    return: reward del episodio
    """
    _ = env.reset()
    rewards = []
    done = False
    while not done:
        action = env.action_space.sample()
        _, reward, done, _ = env.step(action)
        rewards.append(reward)
    
    return agg_func(rewards)

def run_rlmodel_episode_base(rlmodel):
    """
    Función que ejecuta un episodio con un agente de un solo accion
    @param rlmodel: entorno del agente
    return: result del episodio
    """
    result = rlmodel.train()
    return result

def run_rlmodel_episode(rlmodel,agg_func="mean"):
    """
    Función para modelos RL online que ejecuta un episodio con un agente de un solo accion.
    @param rlmodel: entorno del agente
    @param agg_func: función de agregación de los rewards. En caso de ser None devuelve todo el resultado
    return: reward del episodio agregado por la agg_func
    """
    assert agg_func in ["mean", "max","min", None]
    result = run_rlmodel_episode_base(rlmodel)
    return result["episode_reward_{0}".format(agg_func)]

def run_rlmodel_episode_offline(rlmodel, agg_func = None):
    """
    Función para modelos RL offline que ejecuta un episodio con un agente de un solo accion.
    @param rlmodel: entorno del agente
    return: off_policy_estimator
    """
    result = run_rlmodel_episode_base(rlmodel)
    loss = result['info']['learner']['default_policy']['learner_stats']['total_loss']
    model_eval = result["evaluation"]['off_policy_estimator']
    model_eval["loss"] = loss
    return model_eval




def run_simulation(env, num_episodes:int = 1000, func = run_rlmodel_episode, agg_func = np.sum)->list:
    """
    Función que ejecuta una simulación de un agente en un entorno
    @param env: entorno del agente
    @param num_episodes: numero de episodios a ejecutar
    @param func: función que ejecuta un episodio
    @param agg_func: función de agregación de los rewards
    return: reward promedio de los episodios
    """
    rewards = []
    # permite ver el progreso de entrenamiento
    start_time = time.time()
    for i in tqdm(range(num_episodes)):
        rewards.append(func(env, agg_func = agg_func))
    end_time = time.time()
    return rewards, end_time - start_time


def run_one_single_episode(env,trainer,model="bandit", obs = None):
    """
    Función que ejecuta un episodio con un agente de un solo accion
    @param env: entorno del agente
    @param trainer: trainer del agente
    return: None
    """
    
    if obs is None:
        obs = env.reset()


    # Run a single episode.
    done = False
    while not done:
        # Pass the single observation into the `compute_single_action` method of our Trainer.
        action = trainer.compute_single_action(input_dict={"obs": obs})
        if model=="bandit":
            feat_value_of_action = obs["item"][action][0]
            max_choc_feat = obs["item"][np.argmax(obs["item"])][0]
            min_choc_feat = obs["item"][np.argmin(obs["item"])][0]
        
        elif model=="slateq":   
            feat_value_of_action = obs["doc"][str(action[0])][0]
            max_feat_action = np.argmax([value for _, value in obs["doc"].items()])
            max_choc_feat = obs['doc'][str(max_feat_action)][0] 
            min_feat_action = np.argmin([value for _, value in obs["doc"].items()])
            min_choc_feat = obs['doc'][str(min_feat_action)][0] 
        else:
            raise ValueError("model must be 'bandit' or 'slateq'")

        # Print out the picked document's feature value and compare that to the highest possible feature value.
        print(f"action's feature value={feat_value_of_action}; max-feature={max_choc_feat}; min-feature={min_choc_feat}")

        # Apply the computed action in the environment and continue.
        obs, r, done, _ = env.step(action)






