import itertools
import pandas as pd
import numpy as np


def rllib_analysis_to_df(analysis):
    """
    Genera un dataframe con los resultados de un análisis de RLlib
    @param analysis: análisis de RLlib
    return: dataframe con los resultados del análisis
    """
    df_lists = []
    for key, df in analysis.trial_dataframes.items():
        df["logdir"] = key
        df_lists.append(df)
    return pd.concat(df_lists)

def check_prob_len(df, col = "action_prob"):
    """
    Chequea si la longitud de las probabilidades es una única y por tanto solo hay un valor
    @param df: dataframe con las probabilidades de cada acción
    @param col: columna con las probabilidades
    return: True si la longitud de las probabilidades es una única y por tanto solo hay un valor
    """
    act_probs = df[col].to_list()
    act_probs_flatten = set(itertools.chain(*act_probs))
    print(list(act_probs_flatten)[:5])
    return len(set(act_probs_flatten)) == 1

def get_reward_stats(rewards:list)->tuple:
    """
    Devuelve el mean, std, min y max de los rewards
    @param rewards: rewards de una serie de episodios

    """
    return np.nanmean(rewards), np.nanstd(rewards), np.nanmin(rewards), np.nanmax(rewards)

def append_reward_stats(rewards:list, model_name:str,df:pd.DataFrame = None, time_spend:float = None,num_episodes = None)->pd.DataFrame:
    """
    Añade a un dataframe los resultados de la ejecución de un modelo RLlib
    @param rewards: rewards de una serie de episodios
    @param model_name: nombre del modelo
    @param df: dataframe con los resultados de los modelos
    @param time_spend: tiempo que ha tardado en ejecutar el modelo
    @param num_episodes: número de episodios que ha ejecutado el modelo
    return: dataframe con los resultados de los modelos
    """
    mean, min_, max_,std_ = get_reward_stats(rewards)
    
    if df is None:
        df =  pd.DataFrame(columns=["model_name","n_episodes","mean_reward","std_reward","min_reward","max_reward","time_spend"])

    #df.append({"model_name":model_name, "mean":mean, "min":min_, "max":max_}, ignore_index=True)
    df.loc[len(df)] = [model_name, num_episodes,*get_reward_stats(rewards), time_spend]

    return df

