# Deployment 

## Updating a Deployment

$ kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1

$ kubectl edit deployment/nginx-deployment 

## Rolling Back a Deployment 

### Making a error in the version 

$ kubectl set image deployment/nginx-deployment nginx=nginx:1.16.100

$ kubectl rollout status deployment/nginx-deployment

### Checking the revisions of the specific deployment 

$ kubectl rollout history deployment/nginx-deployment

### See the details of the specific revision 

$ kubectl rollout history deployment/nginx-deployment --revision=2

### Rolling Back to the last revision 

$ kubectl rollout undo deployment/nginx-deployment

### Rolling back to the necessary revision 

$ kubectl rollout undo deployment/nginx-deployment --to-revision=2

## Scaling a deployment 

### Normal Scaling

$ kubectl scale deployment/nginx-deployment --replicas=10

### Auto Scaling 

$ kubectl autoscale deployment/nginx-deployment --min=10 --max=15 --cpu-percent=80





