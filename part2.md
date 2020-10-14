# Introduction to geopandas

To follow along with part 2 of this series we will run a Jupyter notebook in Watson Studio. If you have not done so yet, first go through the steps of [part 1](https://github.com/IBMDeveloperUK/Python-Geopandas-Workshop/blob/master/part1.md)

Some additional steps are needed to use GeoPandas and work with geospatial data files. 

### 1. Create a Project Access token

To load the data into a notebook you need an Access Token. 

- Go the Settings tab at the top of the Project and scroll down to `Access tokens`. 
- Click `New token`
- Give the new token a name, select `Editor` and click `Create`

![](/images/token.png)

- You will need this later in the notebook

### 2. Create a custom Python environment

As geopandas is not installed in the default Python environments you need to create a customized environment. This uses `conda create`. But as the environment is running in the Cloud there are a few steps to go through:

- Go to the environments tab at the top of your project
- Click on `new environment definition`

![](/images/new_env.png)

- Give your new environment a name
- Keep the default, select the free hardware configuration `Free - 1 vCPU and 4 GB RAM` and click `Create`

![](/images/customize.png)

- In the next screen you can customize the new environment. Scroll down and click on the `Create` link under Customization

![](/images/customize_env.png)

- A textfield appears that you can edit. Delete all text and copy and paste the below into the textfield:

```# Please add conda channels here
channels:
- defaults
- conda-forge

# Please add conda packages here
dependencies:
- geopandas
- geoplot
- pysal
- folium

# Please add pip packages here
# To add pip packages, please comment out the next line
#- pip:
```
- Click `Apply`

![](/images/customize_env2.png)

- Now you can use this new environment to run notebooks 

## 4. Load and run a notebook

-  Add a new notebook. Click `Add to project` and choose `Notebook`:

![](https://github.com/IBMDeveloperUK/python-geopandas-workshop/blob/master/images/notebook.png)

- Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/Python-Geopandas-Workshop/blob/master/notebooks/part-2-geopandas.ipynb`
- Select the custom runtime enviroment that you created and click `Create Notebook`. 
-  The notebook will load. 
 
You are now ready to follow along with the workshop in the notebook!
