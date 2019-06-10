# Explore UK Crime Data with Pandas and Geopandas

In this workshop you will learn how to expand your Python data analysis skills to geospatial data. The workshop is aimed at people who are interested in data science and data analysis.

During the workshop we will analyse UK Crime Data with Pandas and GeoPandas in a Jupyter notebook. We first will look at the properties of geospatial data and explore the different commands. After you have learned the basics we will go through some exercises analysing the UK Crime Data to explore patterns and trends and create a few maps of crime rates in London.

## Getting Started with Jupyter Notebooks

Jupyter notebooks are an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. 

In this workshop we will use IBM Watson Studio to run a notebook. For this you will need an IBM Cloud account. The following steps will show you how sign up and get started. When you have the notebook up and running we will go through the notebook. 

## IBM Cloud

- [Sign up](https://ibm.biz/Bd2brq) for an IBM Cloud account

- When you are signed up click `Create Resource` at the top of the Resources page. You can find the resources under the hamburger menu at the top left:

 ![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/resources.png)
 
- Search for Watson Studio and click on the tile:

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/studio.png)

- Select the Lite plan and click `Create`.
- Go back to the Resources list and click on your Watson Studio service and then click `Get Started`. 

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/launch.png)

## IBM Watson Studio

### 1. Create a new Project

- You should now be in Watson Studio.
- Create a new project by clicking on `Get Started` and `New Project`, or `Create Project`
- Give your Project a name.
- Select an Object Storage from the drop-down menu or create a new one for free. This is used to store the notebooks and data. **Do not forget to click refresh when returning to the Project page.**
- click `Create`.  

### 2. Create a Project Access token

To load the data into a notebook you need an Access Token. 

- Go the Settings tab at the top of the Project and scroll down to `Access tokens`. 
- Click `New token`
- Give the new token a name, select `Editor` and click `Create`

![](/images/token.png)

- You will need this later in the notebook

### 3. Create a custom Python environment

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

![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/addnotebook.png)

- Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/geopandas-workshop/blob/master/notebooks/geopandas-workshop.ipynb`
- Select the custom runtime enviroment that you created and click `Create Notebook`. 
-  The notebook will load. 
 
You are now ready to follow along with the workshop in the notebook!



