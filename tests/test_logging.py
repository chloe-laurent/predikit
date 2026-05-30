import pytest
from predikit import ModelTool
from unittest.mock import MagicMock

def test_verbose_logging(capsys):
    # 1. Create a fake model that mimics sklearn
    mock_model = MagicMock()
    mock_model.predict.return_value = [1]
    
    # 2. Initialize with verbose=True
    # Note: We include required fields found in the existing tests
    tool = ModelTool(
        model=mock_model, 
        name="test_tool", 
        description="testing logs", 
        verbose=True
    )
    
    # 3. Run the tool using .invoke()
    tool.invoke({"feature1": 10, "feature2": 20})
    
    # 4. Check if the logs printed out
    captured = capsys.readouterr()
    assert "[predikit]" in captured.out
    assert "Latency" in captured.out
