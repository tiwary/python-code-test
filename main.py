from electronics import TV, Laptop, Smartphone

tv = TV()
laptop = Laptop()
smartphone = Smartphone()

# Example tests using the assert statement
assert tv.is_feature_supported('Wi-Fi')
assert not tv.is_feature_supported('Phone Calls')
