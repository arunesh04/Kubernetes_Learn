## RBAC Setup
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

## II. Creating a user

2.1. Set a user entry in kubeconfig

$ kubectl config set-credentials user1 --client-certificate=user1.crt --client-key=user1.key
2.2. Set a context entry in kubeconfig

$ kubectl config set-context user1-context --cluster=minikube --user=user1
You can check that it is successfully added to kubeconfig:

$ kubectl config view
2.3. Switching to the created user

Now, instead of using the minikube context, we want to use user1-context:

$ kubectl config use-context user1-context
$ kubectl config current-context # check the current contextuser1-context
