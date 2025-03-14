#!/bin/bash
set -e

# Change /path/to/folder/ to the folder you are checking
FOLDER_PATH="/home/old-jupyterhub-backup"
BACKUP_FOLDER_NAME="BACKUP"
LINK_NAME="old-jupyterhub" 

# Determine the user's home directory path
USER_HOME=$(eval echo ~$USER)

# Construct the full path for the backup directory in the user's home
BACKUP_PATH="${USER_HOME}/${BACKUP_FOLDER_NAME}"
LINK_PATH="${BACKUP_PATH}/${LINK_NAME}" # Full path of the symlink to be created or deleted

# Check if the source folder exists
if [ -d "${FOLDER_PATH}" ]; then
    echo "Folder exists: ${FOLDER_PATH}"
    
    # Ensure the BACKUP directory exists
    if [ ! -d "${BACKUP_PATH}" ]; then
        echo "Creating BACKUP directory at ${BACKUP_PATH}"
        mkdir "${BACKUP_PATH}"
    fi
    # Create a symbolic link in the BACKUP directory pointing to the specified folder
    if [ -L "${LINK_PATH}" ]; then
        echo "Symbolic link already exists, not doing anything it..."
    else
        ln -s "${FOLDER_PATH}" "${LINK_PATH}"
        echo "Created/Updated symbolic link in ${BACKUP_PATH} named ${LINK_NAME} pointing to ${FOLDER_PATH}"
    fi
else
    echo "Folder does not exist: ${FOLDER_PATH}"
    # If the source folder does not exist but the symlink does, delete the symlink
    if [ -L "${LINK_PATH}" ]; then
        echo "Removing symbolic link as the source folder does not exist..."
        rm "${LINK_PATH}"
    fi
fi