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



# ==============================================================================
# ==============================================================================
# ==============================================================================

# Definir el número de transacciones
num_transactions = 80000

# Generar datos aleatorios para las transacciones
np.random.seed(123)
amounts = np.random.uniform(1, 12000, num_transactions)
dates = [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_transactions)]
fraudulent = np.random.choice([0, 1], num_transactions, p=[0.99, 0.01])

# Crear un DataFrame para almacenar los datos de las transacciones
data = pd.DataFrame({
    'Date': dates,
    'Amount': amounts,
    'Class': fraudulent
})

# Guardar los datos en un archivo CSV
data.to_csv('/datos_transacciones_ejercicio.csv', index=False)

print("Archivo 'datos_transacciones.csv' creado exitosamente.")

