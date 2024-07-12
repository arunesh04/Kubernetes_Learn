1. Check whether RBAC is enabled

$ kubectl api-versions | grep rbac

To enable manually 

$ kube-apiserver --authorization-mode=RBAC

2. Create a Service Account

$ kubectl create serviceaccount demo-user

$ TOKEN=$(kubectl create token demo-user)

3. Configure kubectl with your Service Account

$ kubectl config set-credentials demo-user --token=$TOKEN

$ kubectl config set-context demo-user-context --cluster=rbac-sample --user=demo-user

$ kubectl config current-context

$ kubectl config use-context demo-user-context

$ kubectl get pods
