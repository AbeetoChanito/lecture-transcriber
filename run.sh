
cd client

npm run build
build_exit_code=$?

if [ $build_exit_code -ne 0 ]; then
  echo "Error: npm build failed. Exiting."
  exit 1
fi

python3 ../src/app.py
python_exit_code=$?

if [ $python_exit_code -ne 0 ]; then
  echo "Error: Python script failed. Exiting."
  exit 1
fi

cd ..

echo "Build and execution completed successfully."