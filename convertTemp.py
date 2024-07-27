def convertTemperature(celsius: float) -> list[float]:
        ans = []
        ans.append(celsius  + 273.15)
        ans.append((celsius * 1.8) + 32)
        return ans