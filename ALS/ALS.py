import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder

# Create a Spark session
spark = SparkSession.builder.appName("MovieRatings").getOrCreate()

# Function to load rating data
def get_rating_data():
    schema = StructType([
        StructField("userId", IntegerType(), True),
        StructField("movieId", IntegerType(), True),
        StructField("rating", FloatType(), True),
        StructField("timestamp", IntegerType(), True)
    ])
    data = spark.read.csv('C:\\Users\\Youcode\\Desktop\\Recommandation de Films Jay-Z Entertainment\\Jay-Z-Entertainment-Movie-Recommendation\\api\\data\\u.data', sep='\t', schema=schema, header=False)
    return data

# Load data
movie_ratings = get_rating_data()

# Create test and train set
(training, test) = movie_ratings.randomSplit([0.8, 0.2], seed=42)

# Create ALS model
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating",
          coldStartStrategy="drop", nonnegative=True)

# Tune model using ParamGridBuilder
param_grid = ParamGridBuilder()\
    .addGrid(als.rank, [12, 13, 14])\
    .addGrid(als.maxIter, [18, 19, 20])\
    .addGrid(als.regParam, [0.17, 0.18, 0.191])\
    .build()

# Define evaluator as RMSE
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")

# Build cross-validation using TrainValidationSplit
tvs = TrainValidationSplit(
    estimator=als,
    estimatorParamMaps=param_grid,
    evaluator=evaluator
)

# Fit ALS model to training data
model = tvs.fit(training)

# Extract best model from the tuning exercise using ParamGridBuilder
best_model = model.bestModel

# Generate predictions and evaluate using RMSE
predictions = best_model.transform(test)
rmse = evaluator.evaluate(predictions)

# Save the best model
best_model.write().save("C:/Users/Youcode/Desktop/Recommandation de Films Jay-Z Entertainment/Jay-Z-Entertainment-Movie-Recommendation/ALS/best_model")

# Print evaluation metrics and model parameters
print("RMSE =", rmse)
print("**Best Model**")
print("Rank:", best_model.rank)
print("MaxIter:", best_model._java_obj.parent().getMaxIter())
print("RegParam:", best_model._java_obj.parent().getRegParam())
print("Done")
