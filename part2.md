# Introduction to geopandas

To follow along with part 2 of this series we will run a Jupyter notebook in Watson Studio. If you have not done so yet, first go through the steps of [part 1](https://github.com/IBMDeveloperUK/Python-Geopandas-Workshop/blob/master/part1.md)

An additional step is needed to work with geospatial data files. 

### Create a Project Access token

To load the data into a notebook you need an Access Token. 

- Go the Settings tab at the top of the Project and scroll down to `Access tokens`. 
- Click `New token`
- Give the new token a name, select `Editor` and click `Create`

![](/images/token.png)

- This will be used in the notebook to access a datafile from your Cloud Object Store (COS)

## Load and run a notebook

-  Now add a new notebook. Click `Add to project` and choose `Notebook`:

![](https://github.com/IBMDeveloperUK/python-geopandas-workshop/blob/master/images/notebook.png)

- Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/Python-Geopandas-Workshop/blob/master/notebooks/part-2-geopandas.ipynb`
- Select the default environment with **Python3.7** and click `Create Notebook`. 
-  The notebook will load. 
 
You are now ready to follow along with the workshop in the notebook!
