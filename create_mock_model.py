import numpy as np
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

print("[*] Initializing mock edge classifier generation pipeline...")

# Create structured training data mapping real IoT telemetry dimensions
# Feature 1: Payload Size (Bytes)
# Feature 2: Inter-Arrival Time / IAT (seconds)
X_train = np.array(
    [
        [50.0, 2.0],  # Benign heartbeat telemetry
        [45.0, 1.8],  # Benign telemetry
        [55.0, 2.2],  # Benign telemetry
        [1400.0, 0.01],  # Malicious flood / high payload attack
        [850.0, 0.02],  # Malicious probing vector
    ],
    dtype=np.float32,
)

# Label mapping: 0 = BENIGN (Safe), 1 = CRITICAL ATTACK
y_train = np.array([0, 0, 0, 1, 1], dtype=np.int64)

# Train a lightweight Random Forest classifier optimized for rapid inference
print("[*] Training Random Forest estimator...")
clf = RandomForestClassifier(n_estimators=15, random_state=42)
clf.fit(X_train, y_train)

# Define input tensor schema for ONNX compilation (Batch size = None, Features = 2)
initial_type = [("float_input", FloatTensorType([None, 2]))]

# Compile model into ONNX runtime format
print("[*] Compiling model weights into ONNX binary format...")
onnx_model = convert_sklearn(clf, initial_types=initial_type)

# Save the compiled artifact to disk
model_filename = "model.onnx"
with open(model_filename, "wb") as f:
  f.write(onnx_model.SerializeToString())

print(
    f"[+] Success! Edge-optimized ONNX model saved as '{model_filename}'."
    " Sub-5ms runtime ready."
)