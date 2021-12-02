
<form action="{{data.get('action_url')}}" method="post">
    %for item in data.get('table_headers'):
        %if item.lower() == 'id':
            %continue
        %end
        <input name="{{item}}" type="text" placeholder="{{item}}" />
    %end
    <input value="Submit" type="submit" />
</form>