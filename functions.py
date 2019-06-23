def build(first,last,**user_info):
        profile={}
        profile['first_name']=first
        profile['last_name']=last
        for k,v in user_info.items():
                profile[k]=v
        return profile
fu=build('furqan','elahi',location='karachi',field='engineering')
print(fu)