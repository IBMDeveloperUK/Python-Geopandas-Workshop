# Introduction to Pandas

## Get a free IBM Cloud account <a id="get-a-free-ibm-cloud-account"></a>

To follow along with the workshop start by signing up for a [free Cloud account](https://ibm.biz/BdqCue). After filling in the form, you will receive a verification code by email, so please use a real address.

Once your account is verified and set up, you will see this welcome screen. Click on the 🍔 in the top left corner to expand the contents list. At the top you can find more information about your account, documentation and available resources and services.

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFASNRTG_AZZ4z9-g6%2F-MFFPUi1kAYkYec4NPN8%2FScreenshot%202020-08-21%20at%2010.43.08.png?alt=media&token=67fcecdb-9678-4197-bcc8-d8406fd7b7b4)

Click on the blue button to start adding the resources needed in the workshop.

## Create Resources <a id="create-resources"></a>

### Watson Studio <a id="watson-studio"></a>

You should now see this screen where you can find all available resources:

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFgk0OIudE5WqqqSZN%2F-MFFhXDKJYX2QiTMEB0p%2FScreenshot%202020-08-21%20at%2012.09.25.png?alt=media&token=5b89d5ab-c39d-4449-9dec-2d53fc80da1a)

Search for **Watson Studio** and click on the tile. Choose a region and click **Create**. You can leave all other options as the default:  Free Lite plan and the default name that you will see when scrolling down.

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFgk0OIudE5WqqqSZN%2F-MFFiRs-aDQv5d_D27NL%2FScreenshot%202020-08-21%20at%2012.12.40.png?alt=media&token=84aa1629-9702-427c-810f-91bb9df1716c)

Watson Studio is now ready, but you will need a few other resources as well. Click on **Resource list** to go back:

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFgk0OIudE5WqqqSZN%2F-MFFkILqpjqFjjeTLo8e%2FScreenshot%202020-08-21%20at%2012.21.34.png?alt=media&token=7dd7474f-67ac-4a8a-b656-b1ab24493e03)

From the _Resource list_ click on **Create resource** in the top right to add the next one:

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFgk0OIudE5WqqqSZN%2F-MFFkjFV1soj4MQtiCWC%2FScreenshot%202020-08-21%20at%2012.23.33.png?alt=media&token=784968fb-16f9-4e37-9d8f-e5c89717091e)

### Object Storage <a id="object-storage"></a>

Select **Services** and **Storage** from the menu on the left and search for **Object Storage**. Click on the tile:

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFnjYLeJsutahb0YCG%2F-MFFpTXr9x7GRS6O74fl%2FScreenshot%202020-08-21%20at%2012.44.15.png?alt=media&token=9c692fe5-80f6-4b88-a5b7-cd853766ba6c)

As before use the defaults to create this service in the next screen and then go back to the **Resource list** by clicking first on the 🍔 in the top left corner to expand the contents list:

![](https://gblobscdn.gitbook.com/assets%2F-MFAEq_Dxo1LQbJu5R2R%2F-MFFnjYLeJsutahb0YCG%2F-MFFqHgkzTz0Ngc_-OBD%2FScreenshot%202020-08-21%20at%2012.47.59.png?alt=media&token=9ff51518-1bf3-4f48-b176-e01b6feb8f44)

## Next <a id="next"></a>

In the Resources list click on **Watson Studio** and then on **Get Started** in the next screen:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-08-27-at-13.44.03.png)

This will open a new Tab in your browser where you should now see the below screen:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-08-21-at-16.50.56.png)

## Jupyter notebooks in Watson Studio <a id="jupyter-notebooks-in-watson-studio"></a>

Let's start by setting up a project where you can store data, notebooks and many other assets.

Within the project we will use Jupyter notebooks that allow you to create and share documents containing live code, equations, visualisations and explanatory text. We will be using a number of notebooks in Watson Studio throughout this workshop. These notebooks are contained in a project that you will import into your Watson Studio instance.

### Create a project <a id="create-a-project"></a>

Click on **Start working** to create a project that will contain all the assets for this workshop:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-08-21-at-16.50.56.png)

In the next screen click on **Create an empty project**. Then give your new project a name and click on Create in the bottom right:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-09-03-at-10.50.45.png)

Your previously created Object Storage should be added automatically as above. But it is possible you have to select it from a drop-down menu first.

**Welcome to your new project!** Here you can store notebooks, data and much more. You can also add collaborators, schedule jobs and customise runtime environments. 

Click on **Add to project** at the top right and you will see the below menu with a list of all assets you can add. Click on **Notebook** to add one.

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-09-03-at-10.56.21.png)

This will bring you here, where you can create a new notebook, add one from a local file or from a URL:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-09-03-at-11.22.15.png)

To load the notebook for this workshop, select **From URL**, give the notebook a name, paste the below link to the notebook in the **Notebook URL** field and then click the **Create** button at the bottom right. You can leave the runtime as the default. 

`https://github.com/IBMDeveloperUK/Python-Geopandas-Workshop/blob/master/notebooks/part-1-pandas.ipynb`

### Running a notebook

Now a kernel is being spun up and the notebook loaded:

![](https://github.com/MargrietGroenendijk/gitbooks/blob/master/.gitbook/assets/screenshot-2020-09-03-at-11.28.05.png)

Run each cell in order by selecting it, and then clicking the ▶︎ Run button at the top or use **Shift-Enter**. 
