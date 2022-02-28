# Documentation
First I want to say, that this is still work in progress and few things may change during a process of development. However basic structure is defined already, ready for use with tekton tasks. This documentation will describe step by step how to use those "runners"(docker images capable of executing certain actions). You need to use quay.io registry for checking the clair vulnerabilities. This won't work on others registries.

### Prerequisities
Docker basic knowledge

Python basic knowledge

Shell basic knowledge

CRC cluster with tekton installed

- Repo currently consists of two solutions, one in python and one in shell, this documentation is aplicable for both of them.

## 1. Build & push image

1.1 Clone this git repo with specified branch you want to use.
> git clone --branch alpha-v1 https://github.com/jsztuka/hacbs.git

1.2 Change the folder to the one that consists Dockerfile

1.3 Build docker image
> sudo docker build -t "my-image-name":"tag" . 

1.4 Push your image to public registry(docker.io/quay.io)
> sudo docker push "my-image-name":"tag"

## 2. Create tekton task and run it

2.1 Log into your CRC cluster as admin.

2.2 Apply this tekton task manifest with your data:

```
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: test-clair
spec:
  params:
    - name: sha
      description: Sha256 of an image
      default: "sha256:e33c555044f1333032d414fff5cd1ff0d8f9fe7face8fa3bf54b7b996893d79d" (SHA OF IMAGE IN THE REPO)
      type: string
    - name: repo
      description: Image repository
      default: "cvpops/test-index" (QUAY.IO REPOSITORY PATH TO YOUR IMAGE)
      type: string
  steps:
    - name: get-vulnerabilities
      image:  "my-image-name":"tag"
      args: ['$(params.sha) $(params.repo)']
```
- you can name the task as you want, just so you are able to easily find logs for it
- apply this manifest file in such manner: `kubectl apply -f task-clair.yaml`
- look for logs this way: `tkn task start --showlog test-clair`

That is basically it. Now you should have obtained 

This project is for development purpose only.
Dont be shy.
