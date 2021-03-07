from sklearn.linear_model import LinearRegression

plt.yscale("log")
plt.xscale("log")
# Scatter
plt.xlabel(" Rpeak")
plt.ylabel("nombre de cores")

x = np.array(createTab(2011, 2020, "Rpeak")).reshape(-1,1)
y = np.array(createTab(2011, 2020, "Cores"))


reg = LinearRegression()
predict_space = np.linspace(min(x), max(x)).reshape(-1,1)
reg.fit(x,y)
predicted = reg.predict(predict_space)
print('R^2 score: ',reg.score(x, y))
# Plot regression line and scatter
plt.plot(predict_space, predicted, color='red', linewidth=5)
plt.scatter(x=x,y=y)
plt.xlabel('pelvic_incidence')
plt.ylabel('sacral_slope')
plt.show()
plt.savefig("00003.png", bbox_inches = "tight") 