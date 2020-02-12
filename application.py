#! /usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np 
import pandas as pd
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

coord=np.load("position.npy")
noms=list(np.load("film.npy"))

@app.route('/')
def Test_1():
    return render_template('Test_1.html')


@app.route('/result', methods=['POST','GET'])
def result():
	film=str(request.args.get('film'))

	dist=[]
	nom_inde=noms.index(film)
	for i in range(coord.shape[0]):
		#L2
		dist.append(np.linalg.norm(coord[nom_inde]-coord[i]))

	dist_sor=sorted(dist)
	films=[]
	i=1
	k=6
	while i<k:
		a=dist.index(dist_sor[i])
		b=noms[a]
		if b not in films:	
			films.append(b)
			i+=1
		else:
			i+=1
			k+=1

	return render_template('result.html', film=films) 

if __name__ == '__main__':
    app.run(debug=True)



