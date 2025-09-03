# ai_models/ai_models.py

# Example fraud detection logic (dummy version for now)
# Later you can replace with real ML model loading & prediction

def predict_fraud(transaction_data: dict) -> dict:
    """
    Predict if a transaction is fraudulent.
    
    Args:
        transaction_data (dict): Input features (amount, sender, receiver, etc.)
    
    Returns:
        dict: { "fraud": bool, "confidence": float }
    """
    # ----- Dummy placeholder -----
    # Example: If amount > 10000, mark as fraud
    amount = transaction_data.get("amount", 0)

    if amount > 10000:
        return {"fraud": True, "confidence": 0.85}
    else:
        return {"fraud": False, "confidence": 0.95}
