%Harry Huang 11/16/20

clear
%part (a)
%Parameters
beta_gamma_combos= {{5e-7 0.05} {5e-7 0.05} {10*5e-7 0.05} {10*5e-7 0.05*10} {0.1*5e-7 0.05} {5e-7 0.05*10}};

death_rate= 0.05;

dt= 0.001; %days
maxT= 365; %days
steps= maxT/dt;
time= 0:dt:maxT;
%Initialize or reset category arrays
N= 1e6;
sus= zeros(size(time));
sus(1)= (1e6-10)/N; %All 1 million, except 10, are initial susceptible
infective= zeros(size(time));
infective(1)= 10/N; %Only 10 are initially infective
recovered= zeros(size(time));
deaths= zeros(size(time)); %total deaths over time

for i2=1:6
    beta= beta_gamma_combos{i2}{1}; %infection rate
    gamma= beta_gamma_combos{i2}{2}; %recovery rate



    %Forward Euler
    for i=1:steps
        sus(i+1)= sus(i)-dt*(beta*N*sus(i)*infective(i));
        infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma)*infective(i);
        if i2==2 %if the model incorporates deaths
            infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma-death_rate)*infective(i);
            deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
        end
        recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
    end
    
    if i2==1
        name= 'original parameters';
    elseif i2==2
        name= 'original parameters incorporating deaths';
    elseif i2==3
        name= '10x beta';
    elseif i2==4
        name= '10x beta & 10x gamma';
    elseif i2==5
        name= 'one tenth beta';
    elseif i2==6
        name= '10x gamma';
    end

    f= figure('Name',name); 
    plot(time, sus)
    hold on
    plot(time, infective)
    plot(time, recovered)
    if i2==2
        plot(time, deaths)
    end
    hold off
    title(name+ " over 1 year")
    xlabel('Time(days)')
    ylabel('Fraction of total population')
    legend('Susceptible','Infective','Recovered')
    if i2==2
        legend('Susceptible','Infective','Recovered','Deaths')
    end
    saveas(f,name,'png')
    
    if i2==1
        f=figure('Name', 'S vs I dynamics');
        plot(sus,infective)
        hold on 
        plot(sus,infective==0,':k');
        xline(gamma/(beta*N),':k');
        title ('S vs I dynamics')
        xlabel('fraction susceptible')
        ylabel ('fraction infective')
        saveas(f,'S vs I dynamics','png')
    end
    
end
%%
%part(b)
beta= 5e-7; %infection rate
gamma= 0.05; %recovery rate
death_rate= 0.05;

dt= 0.001; %days
maxT= 365; %days
steps= maxT/dt;
time= 0:dt:maxT;

%Initialize category arrays
N= 1e6;
sus= zeros(size(time));
infective= zeros(size(time));
recovered= zeros(size(time));
deaths= zeros(size(time)); %total deaths over time

for i2=1:2 %If i2=1, quarantine iteration. If i2=2, vaccination iteration
    x=0; %initial threshold multiplier, resets between model iterations
    
    %Initial run to establish baseline deaths
    if i2==1 %quarantine model
        name= 'Quarantine Model';
        %Initial abundances
        sus(1)= (1e6-10)/N; %All 1 million, except 10, are initial susceptible
        infective(1)= 10/N; %Only 10 are initially infective

        %Forward Euler
        for i=1:steps
            sus(i+1)= sus(i)-dt*((1-x)*beta*N*sus(i)*infective(i));
            infective(i+1)= infective(i)+ dt*((1-x)*beta*N*sus(i)-gamma-death_rate)*infective(i);
            recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
            deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            normal_deaths= deaths(length(deaths)); 
        end

    elseif i2==2 %pre-emptive vaccination model
        name= 'Pre-emptive Vaccination Model';
        
        %Initial abundances
        sus(1)= (1e6-(x*1e6)-10)/N; %All 1 million, except x proportion of vaccinated and 10 infective, are initial susceptible
        infective(1)= 10/N; %Only 10 are initially infective
        recovered(1)= x*1e6; %Initial number of vaccinated individuals

        %Forward Euler
        for i=1:steps
            sus(i+1)= sus(i)-dt*(beta*N*sus(i)*infective(i));
            infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma-death_rate)*infective(i);
            recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
            deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            normal_deaths= deaths(length(deaths)); 
        end    
    end
    
    thresholds= {0.5*normal_deaths 0.1*normal_deaths 0.01*normal_deaths};
    
    %Threshold checking loops
    %Check for 50 threshold
    while deaths(length(deaths))>thresholds{1}
        x=x+0.001;
        if i2==1 %quarantine model
            %Initial abundances
            sus(1)= (1e6-10)/N; %All 1 million, except 10, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*((1-x)*beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*((1-x)*beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end

        elseif i2==2 %pre-emptive vaccination model
            %Initial abundances
            sus(1)= (1e6-(x*1e6)-10)/N; %All 1 million, except x proportion of vaccinated and 10 infective, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective
            recovered(1)= x*1e6/N; %Initial number of vaccinated individuals

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*(beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end    
        end
    end
    x1=x; %effectiveness multiplier to reach 50 percent death reduction
    reduction= ' 50%';
    
    f= figure('Name',strcat(name,reduction, ' death reduction over 1 year')); 
    plot(time, sus)
    hold on
    plot(time, infective)
    plot(time, recovered)
    plot(time, deaths)
    hold off
    title(strcat(name,reduction, ' death reduction over 1 year'))
    xlabel('Time(days)')
    ylabel('Fraction of total population')
    legend('Susceptible','Infective','Recovered','Deaths')
    saveas(f,strcat(name,reduction),'png')
    
    %Check for 90 threshold
    while deaths(length(deaths))>thresholds{2}
        x=x+0.01;
        if i2==1 %quarantine model
            %Initial abundances
            sus(1)= (1e6-10)/N; %All 1 million, except 10, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*((1-x)*beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*((1-x)*beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end

        elseif i2==2 %pre-emptive vaccination model
            %Initial abundances
            sus(1)= (1e6-(x*1e6)-10)/N; %All 1 million, except x proportion of vaccinated and 10 infective, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective
            recovered(1)= x*1e6/N; %Initial number of vaccinated individuals

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*(beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end    
        end
    end
    x2=x; %effectiveness multiplier to reach 90 percent death reduction
    reduction= ' 90%';
    
    f= figure('Name',strcat(name,reduction, ' death reduction over 1 year')); 
    plot(time, sus)
    hold on
    plot(time, infective)
    plot(time, recovered)
    plot(time, deaths)
    hold off
    title(strcat(name,reduction, ' death reduction over 1 year'))
    xlabel('Time(days)')
    ylabel('Fraction of total population')
    legend('Susceptible','Infective','Recovered','Deaths')
    saveas(f,strcat(name,reduction),'png')
    
    %Check for 99 threshold
    while deaths(length(deaths))>thresholds{3}
        x=x+0.01;
        if i2==1 %quarantine model
            %Initial abundances
            sus(1)= (1e6-10)/N; %All 1 million, except 10, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*((1-x)*beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*((1-x)*beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end

        elseif i2==2 %pre-emptive vaccination model
            %Initial abundances
            sus(1)= (1e6-(x*1e6)-10)/N; %All 1 million, except x proportion of vaccinated and 10 infective, are initial susceptible
            infective(1)= 10/N; %Only 10 are initially infective
            recovered(1)= x*1e6/N; %Initial number of vaccinated individuals

            %Forward Euler
            for i=1:steps
                sus(i+1)= sus(i)-dt*(beta*N*sus(i)*infective(i));
                infective(i+1)= infective(i)+ dt*(beta*N*sus(i)-gamma-death_rate)*infective(i);
                recovered(i+1)= recovered(i)+dt*(gamma*infective(i));
                deaths(i+1)= deaths(i)+dt*death_rate*infective(i);
            end    
        end
    end
    x3=x; %effectiveness multiplier to reach 99 percent death reduction
    reduction= ' 99%';

    f= figure('Name',strcat(name,reduction, ' death reduction over 1 year')); 
    plot(time, sus)
    hold on
    plot(time, infective)
    plot(time, recovered)
    plot(time, deaths)
    hold off
    title(strcat(name,reduction, ' death reduction over 1 year'))
    xlabel('Time(days)')
    ylabel('Fraction of total population')
    legend('Susceptible','Infective','Recovered','Deaths')
    saveas(f,strcat(name,reduction),'png')
end

  
