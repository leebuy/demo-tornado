#!/bin/sh

\cp supervisord.conf supervisord_deploy.conf
supervisord -c supervisord_deploy.conf
