# Control Plane - Django Example

Required:
1. Control Plane Org
2. Control Plane GVC

Instructions:

1. Clone repository using the command: `git clone git@github.com:controlplane-com/pizza-django.git`
2. Install and login using the Control Plane CLI
3. Build and push image using the command: `cpln image build --name pizza-django:0.1 --push --org ORG_NAME`
4. Create a workload using this image: `cpln workload create --name pizza-django --image //image/pizza-django:0.1 --public --org ORG_NAME --gvc GVC_NAME`
5. That's it!

To Test:

Using the deployed endpoint, the following paths can be browsed to and a sample json can be posted.

1.	https://ENDPOINT/pizza/locations/
-  Use this sample content to post:

```
{
"address": "6724 Yacht Blv",
"city": "Cornwall",
"region": "ON",
"code": "K6H7N6"
}
```
 
 
2.	https://ENDPOINT/pizza/store/10520/menu
- Shows the menu from the location id given in the response to step 1.

3.	https://ENDPOINT/pizza/order
-  This endpoint can take an order post, but don't post and json since it actually hits the Dominos Pizza API.
