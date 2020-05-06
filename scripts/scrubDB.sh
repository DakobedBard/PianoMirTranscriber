sudo docker kill djangoapp
sudo docker cp scripts/remove.sql db:/scrub.sql && sudo docker exec db psql -d db2 -U database1_role -f scrub.sql