## Importamos las librerias necesarias en el proyecto:
# Tratamiento de datos
# ==============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import random
import math

# Preprocesado y modelado
# ==============================================================================
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest
from pyod.utils.data import generate_data, get_outliers_inliers

# Gráficas
# ==============================================================================
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')