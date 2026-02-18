# Set Up Your FRINK Repo in the Landing Zone
Theme 1 Teams, there are several ways to upload your graph to the FRINK Landing Zone found on lakeFS. We recommend uploading through the website for smaller files and using Amazon's S3 Tool for larger files or for automating the process. 

!!! note

    For each method, you will need to request credentials for accessing lakeFS. These credentials are an **Access Key ID** and a **Secret Acess 
    Key**. You may request these either by direct messaging Yaphet Kebede through our PROTO-OKN Slack channel or by emailing Yaphet at kebedey at
    renci dot org. With your request please provide the name of your dataset, that will be used to create a repository to host your data on lakeFS.

!!! warning "File Upload Size Requirements"
   
    Due to technical limits we have some requirements for upload size and tool usage. 
    For files **less than 1G** clients can use **any of the tools** mentioned on this page to upload files. 
    For file sizes **greater than 1G** we recommend using **s3 clients (such as rclone 
    or aws-cli)** as they support chunking large files to small manageable sizes.
    We also recommend using **no parallelization** (this will ensure that our server is  not overwhelmed).



## Repository Structure

Every dataset hosted in FRINK will have its own lakeFS repository. Data submissions should be made by uploading the data to the develop branch of the respective repository. After uploads and commits are completed on the develop branch, the data update can be finalized by creating a merge request to the main branch.

<img src="../../assets/images/branch-struct.png">

## Uploading Data 

### Upload through the website

!!! info inline end ""	

     See the <a href="https://docs.lakefs.io/quickstart/">lakeFS QuickStart guide</a> for more information.</strong></font> 
  


1. Navigate to [https://frink-lakefs.apps.renci.org/](https://frink-lakefs.apps.renci.org/)

2. Enter your **Access Key ID** and your **Secret Access Key** to log in.

3. Browse to your working repository.

4. By default, your repository would be on main branch, double check to make sure that is set to `develop` branch.  
 <img src="../../assets/images/13change-branch.png" width="400">

5. Click the **Upload Object** button to upload your dataset/graph.  
<img src="../../assets/images/3upload-object-button.png" width="600">

6. The **Upload Object** pop-up window will appear offering you the option to drag and drop a single file from your desktop to the pop-up window. Once your file appears in the pop-up, click the **Upload** button to complete the upload. (Although there is a **Path** text field, it will not recognize a file path on your local machine. So please use the drag and drop feature.)
<img src="../../assets/images/4upload-object-popup.png" width="400">     

	!!! warning ""

	 	**Repeat this step for each file you need to upload.** 
	 
7. Your upload is not complete until you commit the change to lakeFS. Click the **Uncommitted Changes** tab and you will see the upload you made in the previous steps. Click the **Commit Changes** button.
<img src="../../assets/images/5uncommitted-changes-tab.png">

8. The **Commit Changes** pop-up window will appear. Please enter a **Commit Message** providing information about the nature of your upload. We suggest you include your name in case multiple individuals from your team are uploading files to lakeFS. The date and time will be recorded automatically.  
<img src="../../assets/images/7commit-changes-popup.png" width="400">



### Upload Using s5cmd

!!! info inline end ""
    s5cmd is a fast S3-compatible command line tool that works seamlessly with lakeFS. More details about s5cmd be found in [this guide](https://github.com/peak/s5cmd).

1. **Install or run s5cmd.**
    You can either install the binary locally or run it using Docker.
   
    - **Option A – Install locally:** Download the latest release from: [https://github.com/peak/s5cmd](https://github.com/peak/s5cmd). Extract the binary and ensure it is available in your system PATH:
        ```bash
             s5cmd version
        ```
    - **Option B – Run with Docker (no local install required):**
         ```bash
              docker run --rm peakcom/s5cmd version
         ```

2. **Configure credentials and lakeFS endpoint.**

    s5cmd uses standard AWS environment variables for authentication.
    - Export your **Access Key ID**, **Secret Access Key**, and the required lakeFS endpoint:
        ```bash
            export AWS_ACCESS_KEY_ID=<your-access-key-id>
            export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
            export LAKEFS_ENDPOINT=https://frink-lakefs.apps.renci.org
   
        ```

3. **Upload files to the repository.**
    - **If installed locally:**
        ```bash
            s5cmd --endpoint-url $LAKEFS_ENDPOINT cp my-local-dataset.hdt s3://my-repo/develop/my-local-graph.hdt
        ```

    - **If running with Docker:**
        ```bash
            docker run --rm \
            -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
            -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
            -v $(pwd):/data \
            peakcom/s5cmd \
            --endpoint-url $LAKEFS_ENDPOINT \
            cp /data/my-local-dataset.hdt s3://my-repo/develop/my-local-graph.hdt
        ```

    This example copies the `my-local-dataset.hdt` file to a repo called `my-repo` on the `develop` branch, renamed as `my-local-graph.hdt`. The `--endpoint-url` option ensures the command targets your lakeFS instance.


4. **Commit the upload.**
    - Back in the web browser, go to your repository.
    - Navigate to the **Uncommitted Changes** tab. Click the **Commit Changes** button.
    - The **Commit Changes** pop-up window will appear. Please enter an appropriate **Commit Message**.
    
    <img src="../../assets/images/7commit-changes-popup.png" width="400">

### Upload from other Storage providers (Azure, S3 etc...)

!!! info inline end ""   
    For more details on rclone commands and options, visit the [rclone documentation](https://rclone.org/docs/).



This guide can serve as a way to configure rclone as a tool to copy files to lakefs. In this guide we will use 
Azure blob storage as an example. 

1. Install rclone

    If you haven't installed rclone yet, you can do so by following the instructions on the [rclone website](https://rclone.org/downloads/).

2. Configure rclone source with Azure Blob Storage
    - **Create a new rclone remote for Azure Blob Storage**:
         Open a terminal and run the following command to configure a new remote:   
         ```
         rclone config
         ```      
    - **Create a new remote**:
        - Type `n` to create new remote and press Enter.
        - Name the remote (e.g. `azureblob`)
    - **Choose the backend**: 
        - When prompted to choose a storage type , select `32` (Microsoft Azure Blob Storage)
    - **Configure the Azure Blob Storge backend**:
      -  Follow the prompts to configure the Azure Blob Storage backend. You will need:
        - `Account Name`: Your Azure Storage account name.
        - `Account Key`: Your Azure Storage account key. 
    - **Save the configuration**:
      - After providing the necessary information, confirm the setup and save the configuration.

3. Configure rclone with lakeFS
    - **Create a new rclone remote for Azure Blob Storage**:
         Open a terminal and run the following command to configure a new remote:
         ```
         rclone config
         ```
    - **Create a new remote**:
        - Type `n` to create new remote and press Enter.
        - Name the remote (e.g. `lakefs`) 
    - **Choose the backend**: 
        - When prompted to choose a storage type , select `5` (S3) and then select `31` (Other) on the next prompt
    - **Configure the lakeFS backend**:
      -  Follow the prompts to configure the lakefs backend. You will need:
        - `AWS Access Key ID`: Your lakeFS access key id .
        - `AWS Secret Access Key`: Your lakefs secret access key.
        - For region leave empty
        - `Endpoint for S3 API`: this is the url for lakefs https://frink-lakefs.apps.renci.org
        - Follow the rest of the prompt according to your needs
    - **Save the configuration**:
      - After providing the necessary information, confirm the setup and save the configuration.
    
4. Verify the Configuration

    You can list the contents of your Azure Blob Storage and lakeFS repository to verify the configuration:
```
rclone ls azureblob:your-container-name
rclone ls lakefs:your-repository-name
```
If the configuration is correct, you should see the contents of your Azure Blob Storage container and lakeFS bucket.

5. Copy Data from Azure Blob Storage to lakeFS

    To copy data from Azure Blob Storage to your lakeFS server, use the rclone copy or rclone sync command. Here's an example using the rclone copy command:
``` 
rclone copy azureblob:your-container-name/path/in/container lakefs:your-repository-name/develop/location/of/file
```